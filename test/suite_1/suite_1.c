#include <unity.h>

#include <module_a.h>


void setUp(void) {
    // set stuff up here
}

void tearDown(void) {
    // clean stuff up here
}

/**
 * @brief All Tests
 * @defgroup all_tests All Tests
 *
 */

/**
 * @brief average tests
 * @defgroup tests_average_three_bytes Average Three Bytes
 * @ingroup all_tests
 * @{
 *
 */
/**
 * @brief test midrange values
 *
 * @verify{@req{001}}
 */
void test_AverageThreeBytes_should_AverageMidRangeValues(void)
{
    TEST_ASSERT_EQUAL_HEX8(40, average_three_bytes(30, 40, 50));
    TEST_ASSERT_EQUAL_HEX8(40, average_three_bytes(10, 70, 40));
    TEST_ASSERT_EQUAL_HEX8(33, average_three_bytes(33, 33, 33));
}

/**
 * @brief test high values
 * @verify{@req{002}}
 */
void test_AverageThreeBytes_should_AverageHighValues(void)
{
    TEST_ASSERT_EQUAL_HEX8(80, average_three_bytes(70, 80, 90));
    TEST_ASSERT_EQUAL_HEX8(127, average_three_bytes(127, 127, 127));
    TEST_ASSERT_EQUAL_HEX8(84, average_three_bytes(0, 126, 126));
}

int main(void)
{
    UNITY_BEGIN();

    RUN_TEST(test_AverageThreeBytes_should_AverageMidRangeValues);
    RUN_TEST(test_AverageThreeBytes_should_AverageHighValues);

    return UNITY_END();
}

/**
 * @}
 *
 */